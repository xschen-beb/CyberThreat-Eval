# Import the tiktoken library
import tiktoken


# Define the class
class Tokenizer:
    """
    A class to tokenize and detokenize input strings using the Hugging Face tokenizers.
    """
    # Initialize the class with the model name
    def __init__(self, model_name):
        # Load the tokenizer from the model name
        self.tokenizer = tiktoken.encoding_for_model(model_name)

    # Define a method to truncate an input string by max token length
    def truncate(self, input_string, max_token_length):
        """This method truncates a string to a maximum token length."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Check if the number of tokens is greater than the max token length
        if len(tokens) > max_token_length:
            # Truncate the tokens by the max token length
            tokens = tokens[:max_token_length]
        # Decode the tokens back to string
        output_string = self.tokenizer.decode(tokens)
        # Return the output string
        return output_string

    # Define a method to split input string into strings of max token length
    def split(self, input_string, max_token_length):
        """This method splits a string into multiple strings of maximum token length."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Initialize an empty list to store the output strings
        output_strings = []
        # Loop through the tokens with a step size of max token length
        for i in range(0, len(tokens), max_token_length):
            # Slice the tokens by the current index and the max token length
            sliced_tokens = tokens[i : i + max_token_length]
            # Decode the sliced tokens back to string
            sliced_string = self.tokenizer.decode(sliced_tokens)
            # Append the sliced string to the output strings list
            output_strings.append(sliced_string)
        # Return the output strings list
        return output_strings

    def count_tokens(self, input_string):
        """This method counts the number of tokens in an input string."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Return the number of tokens
        return len(tokens)
