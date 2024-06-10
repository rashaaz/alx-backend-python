#!/usr/bin/env python3
""" This module contains a function """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Creates and returns an asyncio Task """
    task = create_task(wait_random(max_delay))
    return task
