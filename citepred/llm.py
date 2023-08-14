import json
import logging
import re
from typing import Literal

import openai

logger = logging.getLogger(__name__)


def get_sentiment(
    sentences: list[str], model="gpt-3.5-turbo"
) -> list[Literal["positive", "negative", "neutral", "unknown"] | None]:
    prompt_format = """
    Classify the sentiment of the following sentences from published scientific articles as either "positive", "negative", "neutral", or "unknown":

    --- BEGIN SENTENCES ---
    {sentences}
    --- END SENTENCES ---

    Report the sentement classification of each sentence on a new line with only its corresponding numbered identifier as a JSON object with the format `{{"id": $id, "sentiment": $sentiment}}`.

    Do not include the original sentence or explanation of any kind.

    Sentiment classifications:
    """
    classifications = test_sentences(
        prompt_format, sentences, response_re_type="(positive|negative|neutral|unknown)", response_name="sentiment", model="gpt-3.5-turbo"
    )
    return [classifications.get(i + 1) for i in range(len(sentences))]


def get_readability(
    sentences: list[str], model="gpt-3.5-turbo"
) -> list[int]:
    prompt_format = """
    Find the Flesch reading ease score of the following sentences from published scientific articles:

    --- BEGIN SENTENCES ---
    {sentences}
    --- END SENTENCES ---

    Report the reading ease score of each sentence as an integer on a new line with only its corrisponding numbered identifier as a JSON object with the format '{{"id": $id, "score": $score}}'.
    
    Do not include the original sentence or explanation of any kind.

    Flesch Reading Scores:
    """
    scores = test_sentences(
        prompt_format, sentences, response_re_type="\d+", response_name="score", model="gpt-3.5-turbo"
    )
    return [scores.get(i + 1) for i in range(len(sentences))]


def test_sentences(
    prompt_format: str, sentences: list[str], response_re_type: str, response_name: str, model: str
) -> dict[str, str]:
    clean_sentences = [re.sub("[\r\n]+", "", sentence) for sentence in sentences]
    prompt = prompt_format.strip().format(
        sentences = "\n".join(
            [f'{i+1}. {sentence}' for i, sentence in enumerate(clean_sentences)]
        )   
    )
    logger.debug(f"Prompt:\n{prompt}")
    chat_completion = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    response = chat_completion.choices[0].message.content
    logger.debug(f"Response:\n{response}")
    return {
        (record := json.loads(e.strip()))["id"]: record[response_name]
        for e in response.split("\n")
        if re.match(
            f'{{"id": \d+, "{response_name}": {response_re_type}}}', e.strip()
        )
    }