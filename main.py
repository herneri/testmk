"""
    Copyright 2024 Eric Hernandez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import test
from sys import argv
from os import path, getenv, mkdir

default_root_path = getenv("HOME") + "/.testmk/"
test_path = ""
argc = len(argv)

if argc < 2 or argv[1] == "-h":
	print("usage: testmk [TEST]\n\n-f [PATH]\tRun test at PATH")
	exit(0)

if argv[1] == "-f":
	if argc < 3:
		print("-f requires a specified path")
		exit(1)

	if path.isfile(argv[2]) == False:
		print(f"Test not found in {argv[2]}")
		exit(2)

	test_path = argv[2]
else:
	if path.isdir(default_root_path) == False:
		mkdir(default_root_path)
	
	if path.isfile(default_root_path + argv[1]) == False:
		print("Test not found in ~/.testmk/")
		exit(2)
	
	test_path = default_root_path + argv[1]

questionSet = []
test.readTest(test_path, questionSet)
test.startTest(questionSet)
test.getResults(questionSet)
