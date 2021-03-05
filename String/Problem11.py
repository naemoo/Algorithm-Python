# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# -*- coding: utf-8 -*-
import re


def solution(new_id):
    # 소문자
    new_id = new_id.lower()
    # - num . _
    new_id = re.sub('[^0-9-._a-z]', '', new_id)
    # .두번 -> .
    new_id = re.sub('\.+', '.', new_id)
    # 처음이나 끝에 . 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 빈문자열 a추가
    if not new_id:
        new_id = 'a'
    # 16자 이상 -> 16이상 제거
    if len(new_id) >= 16:
        new_id = new_id[:16]
    # . 제거
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 2자 이하라면 맨 끝 이어 붙이기
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id


a = solution('...!@BaT#*..y.abcdefghijklm')
print(a)
a = ''
print(a[-1])