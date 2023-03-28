
listQA = '''
Q: What is the significance of the number "pi"?
A: Pi is a mathematical constant that represents the ratio of the circumference of a circle to its diameter, approximately equal to 3.14159.

Q: What is the symbol "@" used for in modern communication?
A: The "@" symbol is commonly used in email addresses and social media usernames to separate the user's name from the domain or service name.

Q: What is the numerical value of the Roman numeral "XVIII"?
A: The Roman numeral "XVIII" represents the number 18.

Q: What is the difference between the terms "BC" and "BCE"?
A: Both terms are used to refer to the time period before the birth of Jesus Christ, but "BC" stands for "Before Christ" while "BCE" stands for "Before Common Era".

Q: What is the numerical value of the binary number "1011"?
A: The binary number "1011" represents the decimal value 11.

Q: What is the significance of the symbol "$" in currency?
A: The symbol "$" is used to represent various currencies, including the US dollar, Canadian dollar, and Australian dollar.

Q: What is the numerical value of the octal number "37"?
A: The octal number "37" represents the decimal value 31.

Q: What is the symbol "%" used for in mathematics?
A: The symbol "%" represents the modulo operator, which returns the remainder of a division operation.

Q: What is the difference between "AD" and "CE" in dating?
A: Both terms are used to refer to the time period after the birth of Jesus Christ, but "AD" stands for "Anno Domini" while "CE" stands for "Common Era".

Q: What is the numerical value of the hexadecimal number "FF"?
A: The hexadecimal number "FF" represents the decimal value 255.

Q: What is the numerical value of the square root of 25?
A: The square root of 25 is 5.

Q: What is the significance of the symbol "&" in communication?
A: The symbol "&" is commonly used to represent the word "and" in text and communication.

Q: What is the numerical value of the binary number "1101"?
A: The binary number "1101" represents the decimal value 13.

Q: What is the difference between the terms "CE" and "AD" in dating?
A: Both terms are used to refer to the time period after the birth of Jesus Christ, but "CE" stands for "Common Era" while "AD" stands for "Anno Domini".

Q: What is the numerical value of the Roman numeral "MCMXCIV"?
A: The Roman numeral "MCMXCIV" represents the number 1994.

Q: What is the significance of the symbol "!" in mathematics and programming?
A: The symbol "!" is used to represent the factorial function, which multiplies a number by all the positive integers less than itself.

Q: What is the numerical value of the octal number "57"?
A: The octal number "57" represents the decimal value 47.

Q: What is the difference between the terms "GMT" and "UTC" in time zones?
A: Both terms are used to refer to Coordinated Universal Time, but "GMT" stands for Greenwich Mean Time while "UTC" stands for Coordinated Universal Time.

Q: What is the numerical value of the hexadecimal number "A5"?
A: The hexadecimal number "A5" represents the decimal value 165.

Q: What is the significance of the symbol "#" in social media and technology?
A: The symbol "#" is commonly used to represent a hashtag, which is used to categorize and organize content on social media platforms.


Q: What is the difference between a CV and a resume?
A: A CV (curriculum vitae) is a comprehensive document that lists a person's education, work experience, publications, and other achievements, while a resume is a shorter document that summarizes a person's work experience and qualifications.

Q: What is a cover letter and why is it important?
A: A cover letter is a document that accompanies a job application and provides a brief introduction of the applicant and their qualifications. It's important because it can help distinguish the applicant from other candidates and provide additional information about their skills and experiences.

Q: What is a job interview and how should one prepare for it?
A: A job interview is a meeting between an employer and a job candidate to discuss the candidate's qualifications, experience, and suitability for a particular position. One should prepare for it by researching the company and the position, practicing answers to common interview questions, and dressing appropriately.

Q: What is a performance review and why is it important?
A: A performance review is a process in which an employer evaluates an employee's job performance and provides feedback on areas of strength and areas that need improvement. It's important because it can help employees identify areas for growth and development and ensure that they are meeting their job expectations.

Q: What is networking and why is it important for career development?
A: Networking is the process of establishing relationships with people in your field or industry to exchange information, ideas, and resources. It's important for career development because it can help you learn about job opportunities, gain industry knowledge, and build relationships that can lead to future career opportunities.

Q: What is a job offer and what should you consider before accepting it?
A: A job offer is an offer of employment from an employer to a job candidate. Before accepting it, one should consider factors such as salary and benefits, job responsibilities, work schedule, and opportunities for growth and advancement.

Q: What is a job description and why is it important?
A: A job description is a document that outlines the duties, responsibilities, and qualifications required for a particular job. It's important because it can help job candidates understand what is expected of them in the position and can help employers attract qualified candidates.

Q: What is a job search and what are some tips for conducting one effectively?
A: A job search is the process of looking for employment opportunities. Some tips for conducting one effectively include setting goals, identifying target companies and industries, customizing resumes and cover letters, networking, and following up with employers after applying.

Q: What is a mentor and how can having one benefit your career?
A: A mentor is an experienced professional who provides guidance, advice, and support to a less experienced person in their field. Having a mentor can benefit your career by providing you with insights into the industry, opportunities for learning and growth, and a valuable professional network.

Q: What is a work-life balance and why is it important?
A: Work-life balance refers to the equilibrium between the demands of work and the demands of personal life. It's important because it can help prevent burnout and improve overall well-being, which can lead to increased productivity and job satisfaction.

Q: Hello, can you help me find a job?

A: Hi there! I'd be happy to help you with your job search. What kind of job are you looking for?

Q: I'm not exactly sure, but I have experience in customer service.

A: Great! Have you tried searching on job boards or company websites for customer service positions in your area?

Q: Yes, I have, but I haven't had much luck.

A: Okay, let's try narrowing down your search. Are you interested in full-time or part-time work?

Q: Full-time would be ideal.

A: Alright, and do you have any specific industries or companies in mind?

Q: Not really, I'm open to anything.

A: Understood. I would recommend checking out job boards like Indeed or Glassdoor, and using keywords like "customer service" and "full-time" in your search. You could also consider reaching out to staffing agencies that specialize in customer service roles.

Q: That sounds like a good idea. Thanks for the advice!

A: You're welcome! Let me know if you have any other questions or if there's anything else I can assist you with.'''

import re
import random
import time

from nltk.chat.util import Chat, reflections

class FociChatbot(Chat):
    def __init__(self):
        super().__init__([], reflections)
        p = self._pairs

    def add(self, input, output):
        if isinstance(output, str):
            o = [output]
        else:
            o = output
        self._pairs.append((re.compile(input, re.IGNORECASE), o))


def add_response(input, output):
    f.add(input, output)

def converse():
    f.converse()

def respond(input):
    Ans = f.respond(input)

    for i in Ans:
        print(i,end="")
        time.sleep(0.02)
    print()

def reset():
    global f
    f = FociChatbot()


f = FociChatbot()

add_response('Hi', 'Hello!')
#converse()
add_response('What is your favourite colour', 'Red')
add_response('How old are you', 'I am brand new!')
add_response('Are you a person or a bot', "That's for me to know and you to find out")
#converse()
add_response('I love (.*)', 'What do you love about it?')
#converse()
#respond('I love car')
add_response('I forget (.*)', 'Can you think of why you might forget %1 ?')
#converse()
add_response('I like to (.*)', "I can't %1 at all.")
add_response('I like (.*)', 'Yeah, %1 is my favourite thing.')

Q = []
A = []
for i in listQA.split('\n'):
    if i :
        if 'Q:' in i:
            Q.append(i[3:-1])
        if "A:" in i:
            A.append(i[3:-1])

for q,a in zip(Q,A):
        add_response(q.replace('"',''), a.replace('"',''))

conter = 0
for i in Q:
    try:
        print()
        print('>>',i)
        print()
        respond(i.replace('"',''))
        time.sleep(1)
    except:
        pass
converse()

reset()







































