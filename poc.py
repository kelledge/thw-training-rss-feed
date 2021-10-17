#!/usr/bin/env python3
import sys
import re
from bs4 import BeautifulSoup


class Course:
    def __init__(self, element):
        self.element = element

    @property
    def dates(self):
        e = self.element.select('dl.docData > dd')
        start, end = e
        
        exp = re.compile('(.*?)\. ([0-9]{2}.[0-9]{2}.[0-9]{4}), ([0-9]{2}:[0-9]{2}) Uhr')
        start_groups = exp.match(start.text)
        end_groups = exp.match(end.text)
        print(start_groups.groups())
        print(end_groups.groups())
        return e

    @property
    def link(self):
        # copy-pastah
        e = self.element.select_one('h2 > a')
        return e.get('href')

    @property
    def title(self):
        e = self.element.select_one('h2 > a')
        return e.text

    @property
    def seats_remaining(self):
        e = self.element.select_one('p.courseAction > a')
        if e is None:
            return 0

        exp = re.compile('Noch ([0-9]+) Last-Minute-Plätze verfügbar')
        m = exp.match(e.text)
        
        if len(m.groups()) == 0:
            raise ValueError(f'Failed to parse seats remaing: {e.text}')

        # there is only one group, so attempt to return it
        return int(m.group(1))


class CourseList:
    def __init__(self, element):
        self.element = element

    @property
    def courses(self):
        for e in self.element.select('div.teaserlist > div.course'):
            yield Course(e)


def main(path):
    with open(path) as handle:
        soup = BeautifulSoup(handle, 'html.parser')
    
    # todo: assert len() == 1
    course_list_element = soup.select_one('#main > div > div.courseList')
    course_list = CourseList(course_list_element)
    
    for c in course_list.courses:
        if c.seats_remaining == 0:
            continue

        print(f"Title: {c.title}")
        print(f"\t Sign-up Link: {c.link}")
        print(f"\t Seats Remaining: {c.seats_remaining}")
        print(f"\t Dates: {c.dates}")


if __name__ == '__main__':
    page_path = sys.argv[1]
    main(page_path)