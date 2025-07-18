import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    '''
    Count the number of occurrences of a letter in a word or text.

    Args:
        word (str): The input text to search through
        letter (str): The letter to search for

    Returns:
        int: The number of times the letter appears in the text
    '''
    word = word.lower()
    letter = letter.lower()
    return word.count(letter)

demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="🔠 Letter Counter Tool (MCP Enabled)",
    description="Enter a word and a letter. The tool will count how many times the letter appears in the word."
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)
