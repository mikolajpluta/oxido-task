from openai import OpenAI

article_path = 'tresc_artykulu.txt'
html_output_path = 'artykul.html'

client = OpenAI(
    api_key="put your openAI API key here"
)

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def save_html(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
def generate_html(article_text):

    prompt = """
    Reformat the following article text into HTML using structural tags. 
    Mark places for images using <img src='image_placeholder.jpg' alt='image description prompt'> 
    and add captions under the images using appropriate tags, image description prompt should describe 
    thoroughly how image has to look like, caption stays short and simple. Only return the HTML content without 
    any extra text, comments, or the <body> tag. Just the HTML content between the body tags. Do not add any 
    extra content like footer, etc.
    """
    full_prompt = f"{prompt}\n\n{article_text}"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that formats content in HTML."},
            {"role": "user", "content": full_prompt}
        ]
    )

    return response.choices[0].message.content

try:
    article_content = read_article(article_path)
    html_content = generate_html(article_content)
    save_html(html_content, html_output_path)
    print(f"File {article_path} generated correctly")
except Exception as e:
    print(f"Error occured: {e}")
