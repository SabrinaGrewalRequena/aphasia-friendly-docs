# Results — round 1 (November 2026)

25 test documents (15 English, 10 Spanish), never used for training. Two systems:

- **Basic version**: Claude (`claude-sonnet-5-5`) with the rules in `prompts/system.md` and 2 example pairs.
- **Trained model**: Qwen3-4B-Instruct-2507 fine-tuned with LoRA on 125 SLP-approved pairs
  (3 epochs, 48 steps, ~11 min on a free Colab T4; training loss 0.98 → 0.33).

## Automatic checks

| | Basic version | Trained model |
|---|---|---|
| Valid handout produced | 25 / 25 | 24 / 25 (1 stuck in a repetition loop) |
| Every fact copied exactly (fact check) | 24 / 25 (the 1 flag is "1 time a day" for "once daily", a strict-checker false alarm) | 14 / 25 |
| Reading grade ≤ 5 | 25 / 25 (avg 1.6) | 24 / 24 (avg 1.7) |
| Format-rule issues per handout | 0.4 | 2.5 |

Trained-model safety problems found by the fact check: an antibiotic dose dropped; a member ID digit changed and
an invented number from its own arithmetic; crisis numbers (988/911) not placed on emergency lines in 3 handouts;
6 handouts left out minor details without listing them in `omitted`.

## SLP blind review

The 49 handouts (25 basic + 24 trained), labelled A/B so the reviewer could not tell which system made each, were
reviewed by a CCC-SLP (anonymous) on 2026-11-15. **The SLP reported no errors.**

## Conclusion

Both systems write at a very low reading level. The basic version is the safer engine and is chosen for the tool and
the library, always together with the automatic fact check. The trained model is the free, private (offline)
option; it needs exact-copy decoding and check-and-retry before use.
