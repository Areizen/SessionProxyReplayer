#!/bin/bash
mitmdump -ns "./script/session_changer.py $2 $3" -r $0 -w $1
