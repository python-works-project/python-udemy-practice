## お手本コード

### 構成
```
roboter/
├── controller/      ← 会話の流れを制御（司令塔）
│   └── [conversation.py](#roboter---controller---conversation.py)
├── models/          ← データ処理（CSV・ロボットの動作）
│   ├── ranking.py
│   └── robot.py
├── templates/       ← メッセージテンプレート
│   ├── hello.txt
│   ├── greeting.txt
│   ├── which_restaurant.txt
│   └── good_by.txt
├── views/           ← 画面表示（テンプレート読み込み）
│   └── console.py
└── main.py          ← アプリの入口
```

### 処理の流れ
#### roboter / main.py
```python
import roboter.controller.conversation
roboter.controller.conversation.talk_about_restaurant()
```
#### roboter / controller / conversation.py
```python
"""Controller for speaking with robot"""
from roboter.models import robot

def talk_about_restaurant():
    """Function to speak with robot"""
    restaurant_robot = robot.RestaurantRobot()
    restaurant_robot.hello()
    restaurant_robot.recommend_restaurant()
    restaurant_robot.ask_user_favorite()
    restaurant_robot.thank_you()
```
#### roboter / models / robot.py
```python
"""Defined a robot model """
from roboter.models import ranking
from roboter.views import console


DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',
                 speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break


class RestaurantRobot(Robot):
    """Handle data model on restaurant."""

    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.ranking_model = ranking.RankingModel()

    def _hello_decorator(func):
        """Decorator to say a greeting if you are not greeting the user."""
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def recommend_restaurant(self):
        """Show restaurant recommended restaurant to the user."""
        new_recommend_restaurant = self.ranking_model.get_most_popular()
        if not new_recommend_restaurant:
            return None

        will_recommend_restaurants = [new_recommend_restaurant]
        while True:
            template = console.get_template('greeting.txt', self.speak_color)
            is_yes = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
                'restaurant': new_recommend_restaurant
            }))

            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                    not_list=will_recommend_restaurants)
                if not new_recommend_restaurant:
                    break
                will_recommend_restaurants.append(new_recommend_restaurant)

    @_hello_decorator
    def ask_user_favorite(self):
        """Collect favorite restaurant information from users."""
        while True:
            template = console.get_template(
                'which_restaurant.txt', self.speak_color)
            restaurant = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
            }))
            if restaurant:
                self.ranking_model.increment(restaurant)
                break

    @_hello_decorator
    def thank_you(self):
        """Show words of appreciation to users."""
        template = console.get_template('good_by.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name,
        }))
```
#### roboter / models / ranking.py
```python
"""Generates ranking model to write to CSV

TODO (jsakai) Rewrite to DB instead of CSV
"""
import collections
import csv
import os
import pathlib


RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'


class CsvModel(object):
    """Base csv model."""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()


class RankingModel(CsvModel):
    """Definition of class that generates ranking model to write to CSV"""
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        super().__init__(csv_file, *args, **kwargs)
        self.column = [RANKING_COLUMN_NAME, RANKING_COLUMN_COUNT]
        self.data = collections.defaultdict(int)
        self.load_data()

    def get_csv_file_path(self):
        """Set csv file path.

        Use csv path if set in settings, otherwise use default
        """
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path

    def load_data(self):
        """Load csv data.

        Returns:
            dict: Returns ranking data of dict type.
        """
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMN_NAME]] = int(
                    row[RANKING_COLUMN_COUNT])
        return self.data

    def save(self):
        """Save data to csv file."""
        # TODO (jsakai) Use locking mechanism for avoiding dead lock issue
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })

    def get_most_popular(self, not_list=None):
        """Fetch the data of the top most ranking.

        Args:
            not_list (list): Excludes the name on the list.

        Returns:
            str: Returns the data of the top most ranking
        """
        if not_list is None:
            not_list = []

        if not self.data:
            return None

        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        for name in sorted_data:
            if name in not_list:
                continue
            return name

    def increment(self, name):
        """Increase rank for the give name."""
        self.data[name.title()] += 1
        self.save()
```
#### console.py
```python
"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor


def get_template_dir_path():
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    Args:
        template_file_path (str): The template file path
        color: (str): Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    Returns:
        string.Template: Return templates with characters in templates.
    """
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
```
#### good_by.txt
```python
$robot_name: $user_nameさん。ありがとうございました。
$robot_name: Thank you so much, $user_name!

良い一日を！さようなら。
Have a good day!
```

#### greeting.txt
```python
私のオススメのレストランは、$restaurantです。
I recommend $restaurant restaurant.

このレストランは好きですか？ [Yes/No]
Do you like it? [y/n]
```
#### hello.txt
```python
こんにちは！私は$robot_nameです。あなたの名前は何ですか？
Hello, I am $robot_name. What is your name?
```
#### which_restaurant.txt
```python
$user_nameさん。どこのレストランが好きですか？
$user_name, which restaurants do you like?
```
