# Black Box API Challenge – Report

This report summarizes the reverse-engineered behavior of the undocumented endpoints hosted at https://blackbox-interface.vercel.app. Each endpoint was tested with various inputs to understand and document its hidden logic.

## 1. POST /data

- Input: "OpenAI"
- Output: { "result": "Ik9wZW5BSSI=" }
- Decoded Result: "OpenAI" (with quotes)

Inference:  
This endpoint encodes the input string using Base64, but first wraps the input in double quotes. For example, "OpenAI" becomes "Ik9wZW5BSSI=" which decodes to "OpenAI".

## 2. GET /time

- Output: { "result": 8147243 }

Inference:  
Returns a numeric value that does not match any standard timestamp format. This is likely a decrementing internal counter or a custom tick value.

## 3. POST /fizzbuzz

- Input: ["OpenAI"]
- Output: { "result": false }

Inference:  
Despite providing a valid JSON array, the result is always false. The endpoint may have very strict internal rules or could be a decoy. There is no evidence of classic FizzBuzz logic in the output.

## 4. POST /zap

- Input: "OpenAI"
- Output: { "result": "\"OpenAI\"" }

Inference:  
Returns the JSON-stringified version of the input. That means the original string is returned with escaped double quotes.

## 5. POST /alpha

- Input: "OpenAI"
- Output: { "result": false }

Inference:  
The endpoint returns false even for valid alphabetic input. The internal condition for returning true remains unknown and could involve hidden rules or checks.

## 6. POST /glitch

Examples:

- Input: "OpenAI"  
  Output: { "result": "\"IepOn\"A" }

- Input: "Fizzbuzz"  
  Output: { "result": "ziu\"Fzz\"zb" }

Inference:  
The output is a modified version of the input with characters rearranged and extra quotation marks inserted. The logic is non-deterministic and might involve random shuffling, position-based mutation, or string corruption algorithms.

## Summary Table

| Endpoint     | Behavior Summary                                              |
|--------------|---------------------------------------------------------------|
| /data        | Base64-encodes the input after wrapping it in quotes          |
| /time        | Returns a non-standard numeric counter or tick                |
| /fizzbuzz    | Always returns false; no clear logic identified               |
| /zap         | Returns input wrapped in escaped double quotes                |
| /alpha       | Returns false even for alphabetic input; logic unclear        |
| /glitch      | Rearranges input and adds quotes; custom transformation logic |

## Conclusion

The Black Box API challenge tested skills in input crafting, pattern recognition, and reverse engineering. Some endpoints had clear, deterministic behavior, while others involved obscure or misleading logic. Understanding each one required systematic testing and interpretation of subtle behavior patterns.
