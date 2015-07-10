#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zhihu import Question

url = "http://www.zhihu.com/question/25378124"
question = Question(url)
answers = question.get_all_answers()
for answer in answers:
    answer.to_txt()
    answer.to_md()
