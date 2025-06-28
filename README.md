# Black Box Challenge – API Analysis

This repository contains a reverse-engineered analysis of the undocumented API endpoints presented in the Black Box Challenge.

## Methodology

The behavior of each endpoint was deduced through manual testing and scripted requests. The challenge interface at [blackbox-interface.vercel.app](https://blackbox-interface.vercel.app) was used to experiment with inputs and observe outputs. A Python script was also developed to automate and verify findings.

## Summary

The challenge involved identifying the functionality of several unknown API routes. Through careful input manipulation and output observation, each endpoint’s behavior was inferred. The results have been replicated in a mock API server included in this repository.

## Contents

- `main.py` – Mock API server simulating observed endpoint behaviors
- `requirements.txt` – Python dependencies
- `report.md` – Detailed analysis of each endpoint (see separately)
