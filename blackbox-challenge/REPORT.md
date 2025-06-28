# Black Box Challenge – API Behavior Report

# Overview

This report outlines the findings from analyzing several undocumented API endpoints as part of the Black Box Challenge. The primary goal was to investigate how each endpoint functions by supplying different inputs and interpreting the responses. Both browser-based inspection and Python-based automation were employed for this analysis.

# Behavior Summary

# POST /data
Expected Input: A simple string.
Behavior: Returns the Base64-encoded form of the input string.
Example: "hello" → "aGVsbG8="
Inference: Functions as a Base64 encoder.
# GET /time
Expected Input: None.
Behavior: Responds with the current server timestamp in ISO format.
Example Output: {"time": "2025-06-28T08:32:40.000Z"}
Inference: Provides real-time clock output from the server.
# POST /fizzbuzz
Expected Input: A JSON array of strings (usually numbers in string format).
Behavior: Each item is interpreted as a number and evaluated using the classic FizzBuzz rules:
Divisible by 3 & 5 → "FizzBuzz"
Divisible by 3 → "Fizz"
Divisible by 5 → "Buzz"
Otherwise → the number itself as a string.
Invalid strings → return false.
Example: ["3", "5", "15", "abc"] → ["Fizz", "Buzz", "FizzBuzz", false]
Inference: Implements a FizzBuzz evaluator on parsed string inputs.
# POST /zap
Expected Input: A string.
Behavior: Returns the exact same string.
Example: "test" → "test"
Inference: Basic echo endpoint – may be used for connectivity checks or dummy input testing.
# POST /alpha
Expected Input: A string.
Behavior: Returns true only if the input contains alphabet letters only (no digits or symbols).
Examples:
"abc" → true
"abc123" → false
Inference: Validates alphabetic strings.
# POST /glitch
Expected Input: A string.
Behavior: Returns the reverse of the given string.
Example: "world" → "dlrow"
Inference: Performs string reversal — may be a string manipulation test endpoint.

