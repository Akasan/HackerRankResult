#!/bin/bash
ROW=63
COLUMN=100

for((i=0; i<$ROW; i++));do
		printf "%0.s-\n" {1..$COLUMN}
done
