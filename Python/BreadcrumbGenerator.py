#   Nilton Gomes Martins Junior
#   23/07/2018
#   CodeWars - Breadcrumb Generator
#   https://www.codewars.com/kata/563fbac924106b8bf7000046/train/python

def generate_bc(url, separator):

    #   Three cases:
    #   1st case: Only main URL, i.e., only one occurence of a "/" in the URL
    #   2nd case: URL with sub-directories (links) that DOES end with an "index"
    #   3rd case: URL with sub-directories (links) that DOES NOT end with an "index"
    #   For cases 2 and 3, in case the sub-directory is longer than 30 characters (many words separated by "-"), it should be acronymized (except for the words in the array: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"])

    #   1st case
    if url.count('/') == 0:
        return '<a href="/">HOME</a>'
    
    #   The following disregards the extension of the file (.html, .php., .asp, etc.)
    if '.' in url:
        url = url[:url.index('.')]
    
    #   Prepares an output variable for this function
    output = []
    
    #   2nd case
    if url[-5:] == 'index':
        output.append('<a href="/">HOME</a>')
        url = url[:url.index('/') + 1]
        while '/' in url:
            tag = url[:url.index('/')]
            if len(tag) > 30:
                tag = ''.join([word[0] for word in tag.split('-') if word not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]])
            output.append(tag.upper())
            
    while True:
        
        

    return 

def main():
    return

if __name__ == "__main__":
    main()