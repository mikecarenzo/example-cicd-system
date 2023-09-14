class PageGenerator:
    def __init__(self, text):
        """
        Creates a PageGenerator.

        Args:
            text (str): The page's text.
        """
        if isinstance(text, str):
            self.__text = text
        else:
            raise TypeError("String expected.")

    def generate(self):
        """
        Generates a page.

        Returns:
            str: The generated page.
        """
        return (
            """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Generated Page</title>
                </head>
                <body style="background: #434343; color: #ffffff;">
                    <h1 style="font-family: sans-serif;">Generated Page</h1>
                    <p style="font-family: sans-serif;">Generated Page Text:</p>
                    <p style="font-family: sans-serif;">"""
            + self.__text
            + """</p>
                </body>
            </html>
        """
        )
