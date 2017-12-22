#!/bin/bash
mitmdump -ns "./script/session_changer.py $3 $4" -r $1 -w $2 --anticache
