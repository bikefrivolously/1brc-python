#!/usr/bin/env python3

import cProfile

import obrc  # noqa

cProfile.run("obrc.do_calc('../1brc/measurements_small.txt')", "profile_results")
