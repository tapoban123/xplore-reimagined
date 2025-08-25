# Xplore Backend

Generate me 20 psychometric questions with 4 choices for each. The user will answer those psychometric questions and
you will have to analyse the best 3 career choices for the user from the answers to those questions.

You are a professional Career Counselor cum Psychiatrist.
Provided below is are 20 questions and their answers as answered by the user.
I want you to,
1. Analyse the answers well
2. Understand the intellect and other psychometrics' level of the student.
3. Return me 3 most suitable career options for the user.
The career choices to be returned must be appropriate and practical for an Indian user.

#### Example Input:

{
  "details": "success",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJlMmZlMmY4ODAzYjA0NmM5YjMwMjFkMjBiNGQ5YmUxZSIsImV4cCI6MTc1ODcyNTIzMH0.0E75EIwfemhdsFYyXpX7G2LJ29iavnSRUaIFW5YjisA"
}


{
  "details": "success",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxMTNlOWJhNmJkZDY0YjdhYjNhM2MyMzUwZmQ1NDQ4MiIsImV4cCI6MTc1ODczNTA1NH0.8LmQTfwG7pxbJtqTEgdEDpsYxTzcnA1fr0avhoDxjsc"
}


{
"questions_with_answers": [
{
"question": "When working on a group project, what role do you naturally take?",
"answer": "I enjoy organizing tasks and making sure everyone contributes."
},
{
"question": "Which activity sounds most appealing to you?",
"answer": "Designing a poster or visual layout for an event."
},
{
"question": "How do you usually make decisions?",
"answer": "I weigh all possible outcomes before acting."
},
{
"question": "When facing a new problem, what’s your approach?",
"answer": "I analyze the root cause before jumping to solutions."
},
{
"question": "How do you handle tight deadlines?",
"answer": "I focus intensely and prioritize tasks to meet the deadline."
},
{
"question": "What kind of books or articles do you usually enjoy?",
"answer": "Biographies and human behavior-related content."
},
{
"question": "Which of the following best describes your ideal work setting?",
"answer": "A flexible environment where I can work independently on creative tasks."
},
{
"question": "How do you feel about public speaking?",
"answer": "I enjoy it and feel confident expressing my ideas to a group."
},
{
"question": "You are assigned a repetitive task. How do you feel about it?",
"answer": "I get bored quickly and prefer variety in my work."
},
{
"question": "How do you respond when someone disagrees with your idea?",
"answer": "I listen carefully and try to understand their perspective."
},
{
"question": "What drives you to complete a challenging task?",
"answer": "The sense of achievement and solving something complex."
},
{
"question": "In a conflict situation, you usually...",
"answer": "Try to mediate and understand both sides to resolve it peacefully."
},
{
"question": "Which statement best matches your mindset?",
"answer": "I enjoy thinking abstractly and exploring new ideas."
},
{
"question": "How do you prefer to work on tasks?",
"answer": "I like to plan and follow a clear step-by-step structure."
},
{
"question": "Which subject did you enjoy the most in school?",
"answer": "Literature and history."
},
{
"question": "How would you react if your team fails a project?",
"answer": "I’d reflect on what went wrong and support the team emotionally."
},
{
"question": "If given a chance to start a club at school/college, what would it be?",
"answer": "A mental health awareness or peer support group."
},
{
"question": "How do you handle multitasking?",
"answer": "I prefer focusing on one task at a time for better results."
},
{
"question": "When learning something new, what helps you the most?",
"answer": "Hands-on practice or visuals that help me apply the concept."
},
{
"question": "What kind of career excites you the most?",
"answer": "One that allows me to help others and make a real difference."
}
]
}

{
  "careers": [
    {
      "career": "Clinical Psychologist / Counselor",
      "explanation": "Your exceptionally high emotional intelligence, empathy, and strong interest in human behavior and mental health align perfectly with this field. You also possess strong analytical and communication skills essential for understanding and helping clients."
    },
    {
      "career": "UX/UI Designer",
      "explanation": "Your high creativity, design interest, and keen attention to detail are well-suited for creating intuitive and aesthetically pleasing user experiences. Your empathy and problem-solving skills will help you understand user needs and design effective solutions."
    },
    {
      "career": "Human Resources (HR) Specialist / Organizational Development Consultant",
      "explanation": "This role leverages your strong emotional intelligence, empathy, and communication skills to support and develop people within an organization. Your ability to mediate conflicts, understand diverse perspectives, and organize tasks would be highly valuable."
    }
  ],
  "psychometrics": [
    {
      "parameter": "Analytical Thinking",
      "score": 8.5
    },
    {
      "parameter": "Creativity",
      "score": 9
    },
    {
      "parameter": "Emotional Intelligence",
      "score": 9.5
    },
    {
      "parameter": "Leadership",
      "score": 7.5
    },
    {
      "parameter": "Communication Skills",
      "score": 8.5
    },
    {
      "parameter": "Risk-taking",
      "score": 3
    },
    {
      "parameter": "Attention to Detail",
      "score": 8.5
    },
    {
      "parameter": "Problem-solving",
      "score": 8.5
    },
    {
      "parameter": "Empathy",
      "score": 9.5
    },
    {
      "parameter": "Teamwork",
      "score": 8
    },
    {
      "parameter": "Independence",
      "score": 8
    },
    {
      "parameter": "Decision-making",
      "score": 7
    },
    {
      "parameter": "STEM Interest",
      "score": 4
    },
    {
      "parameter": "Humanities Interest",
      "score": 9.5
    },
    {
      "parameter": "Business Interest",
      "score": 4
    },
    {
      "parameter": "Design/Arts Interest",
      "score": 8.5
    },
    {
      "parameter": "Social Work Interest",
      "score": 9.5
    }
  ],
  "report": "https://res.cloudinary.com/dduagzkor/raw/upload/v1755936677/report_50c2e9683aa64abd88c5ae2f7593318d.pdf"
}