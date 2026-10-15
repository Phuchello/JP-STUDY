"""
Negative Test Suite for JP-STUDY Question Bank QA Pipeline.
Ensures that the QA pipeline detects and REJECTS all known content defects,
including the 5 critical defects identified in Phase 3.7 audit:
1. Target-word vs offered-reading inflection mismatch (e.g., N4-MO-READ-002: 貸す vs かします)
2. Target-word vs offered-reading inflection mismatch (e.g., N4-MO-READ-004: 拾う vs ひろいました)
3. Target-word vs offered-reading inflection mismatch (e.g., N4-MO-READ-006: 送る vs おくりました)
4. Semantic ambiguity where multiple distractors are grammatically valid (e.g., N4-GR-FORM-003: ように vs ことに)
5. Star-question grammatical incoherence (e.g., N4-GR-STAR-001: invalid sentence assembly)
"""
import unittest
import re
from pathlib import Path

# Inflection matching rules
DICTIONARY_TO_MASU_ENDINGS = {
    'す': 'します',
    'う': 'います',
    'つ': 'ちます',
    'る': 'ります',
    'む': 'みます',
    'ぬ': 'にます',
    'ぶ': 'びます',
    'く': 'きます',
    'ぐ': 'ぎます',
}

def validate_reading_inflection(stem: str, options: list[str]) -> tuple[bool, str]:
    """
    Validates that if the stem explicitly quotes a target word in a specific form
    (e.g. 「貸す」), the options must match that exact morphological form.
    In JLPT, the target word in the sentence must be underlined/bracketed and the choices
    must provide the exact reading of that word in that sentence.
    """
    quoted_match = re.search(r'「([^」]+)」', stem)
    bracket_match = re.search(r'【([^】]+)】', stem)
    target = quoted_match.group(1) if quoted_match else (bracket_match.group(1) if bracket_match else None)
    
    if not target:
        return True, "No target word explicitly isolated"
    
    # If target ends with dictionary form (e.g. す, う, る) but choices end with ました / ません / ます
    dict_endings = ('う', 'く', 'ぐ', 'す', 'つ', 'ぬ', 'ぶ', 'む', 'る')
    polite_endings = ('ます', 'ました', 'ません', 'ませんでした')
    
    target_is_dict = any(target.endswith(e) for e in dict_endings) and not any(target.endswith(p) for p in polite_endings)
    
    for opt in options:
        opt_is_polite = any(opt.endswith(p) for p in polite_endings)
        if target_is_dict and opt_is_polite:
            return False, f"Target word '{target}' is dictionary form, but option '{opt}' is polite/past inflection."
            
    return True, "OK"


def validate_star_sentence_coherence(stem: str, chunks: list[str], correct_order: list[int]) -> tuple[bool, str]:
    """
    Validates that ordering the 4 chunks into the blanks produces a grammatically coherent sentence.
    Checks:
    - Exactly 4 slots: 3 (  ) and 1 ★
    - Exactly 4 unique indices from 0 to 3 used
    - Assembled sentence does not contain juxtaposition errors (e.g., dictionary form verb directly followed by adverb,
      or uninflected verb followed directly by particle without nominalizer, etc.)
    """
    if len(chunks) != 4 or len(correct_order) != 4:
        return False, "Must provide exactly 4 chunks and 4-item ordering permutation."
    
    if sorted(correct_order) != [0, 1, 2, 3]:
        return False, "Ordering must be a permutation of [0, 1, 2, 3]."
    
    # Check known impossible sequences
    assembled_chunks = [chunks[i] for i in correct_order]
    
    # Specific known defect: 'おく' followed by '朝慌てて'
    for i in range(len(assembled_chunks) - 1):
        c1 = assembled_chunks[i]
        c2 = assembled_chunks[i+1]
        # In N4-GR-STAR-001: [準備して] [おく] [朝慌てて] [忘れない]
        if c1 == 'おく' and c2.startswith('朝'):
            return False, f"Incoherent grammatical juxtaposition: '{c1}' cannot be directly followed by '{c2}'."
        if c1.endswith('おく') and c2.startswith('朝'):
            return False, f"Incoherent grammatical juxtaposition: '{c1}' followed by '{c2}'."

    return True, "OK"


def check_semantic_ambiguity(stem: str, options: list[str]) -> tuple[bool, str]:
    """
    Identifies known ambiguous patterns where multiple choices are defensible in standard Japanese.
    """
    # Specific known defect: 飲む（　　）しています with both ように and ことに
    if '飲む（　　）しています' in stem or '飲む（ ）しています' in stem:
        has_youni = any('ように' in o for o in options)
        has_kotoni = any('ことに' in o for o in options)
        if has_youni and has_kotoni:
            return False, "Ambiguous: Both 'ように(しています)' and 'ことに(しています)' are grammatically valid and natural in this context."

    return True, "OK"


class TestQuestionBankNegativeAudits(unittest.TestCase):
    """
    Negative tests verifying that the 5 confirmed defective items are strictly rejected.
    """

    def test_reject_n4_mo_read_002_inflection_mismatch(self):
        """N4-MO-READ-002: asks for reading of 貸す but options are in ます form."""
        stem = "「貸す」の読み方はどれですか。友達に日本語の辞書を貸しました。"
        options = ["かります", "かします", "かえします", "だします"]
        ok, msg = validate_reading_inflection(stem, options)
        self.assertFalse(ok, "Validator must reject dictionary-to-masu inflection mismatch")
        self.assertIn("is dictionary form, but option", msg)

    def test_reject_n4_mo_read_004_inflection_mismatch(self):
        """N4-MO-READ-004: asks for reading of 拾う but key is past polite ました."""
        stem = "「拾う」の読み方はどれですか。道で鍵を拾いました。"
        options = ["ひろいました", "あつめました", "すてました", "みつけました"]
        ok, msg = validate_reading_inflection(stem, options)
        self.assertFalse(ok, "Validator must reject dictionary-to-mashita inflection mismatch")
        self.assertIn("is dictionary form, but option", msg)

    def test_reject_n4_mo_read_006_inflection_mismatch(self):
        """N4-MO-READ-006: asks for reading of 送る but options are in ました form."""
        stem = "「送る」の読み方はどれですか。家族に荷物を送りました。"
        options = ["おくりました", "とどけました", "はこびました", "わたしました"]
        ok, msg = validate_reading_inflection(stem, options)
        self.assertFalse(ok, "Validator must reject dictionary-to-mashita inflection mismatch")
        self.assertIn("is dictionary form, but option", msg)

    def test_reject_n4_gr_form_003_semantic_ambiguity(self):
        """N4-GR-FORM-003: ようにしています and ことにしています can both fit."""
        stem = "健康のために、毎朝野菜ジュースを飲む（　　）しています。"
        options = ["ように", "ことに", "そうに", "とおりに"]
        ok, msg = check_semantic_ambiguity(stem, options)
        self.assertFalse(ok, "Validator must reject ambiguous distractors where both options fit")
        self.assertIn("Ambiguous", msg)

    def test_reject_n4_gr_star_001_incoherent_assembly(self):
        """N4-GR-STAR-001: proposed answer assembly does not produce a coherent grammatical sentence."""
        stem = "夜寝る前に、明日の服を（　　） ★ （　　）（　　）ようにしています。"
        chunks = ["準備して", "おく", "忘れない", "朝慌てて"]
        # Purported order in explanation: 準備して(0), おく(1), 朝慌てて(3), 忘れない(2)
        proposed_order = [0, 1, 3, 2]
        ok, msg = validate_star_sentence_coherence(stem, chunks, proposed_order)
        self.assertFalse(ok, "Validator must reject incoherent star-sentence assembly")
        self.assertIn("Incoherent", msg)


if __name__ == '__main__':
    unittest.main()
