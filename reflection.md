# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I ran the game, I did insert a few numbers. I then noticed it was completely off when it accepted negative number and numbers over 100. But otherwise it looked like a regular guessing numbers game

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  The hints were backwards, and accepted number that weren't in the range, along with the answer being a negative number
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

onde example when i inserted 0 it said go lower ! it shouldnt take anything other than number between 1 - 100
when I inserted 123 it said go higher again same error with the first one
when I entered 25 it said go lower inconsistent logic
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code. I had claude point out where the issue may be lying and they figured out where and explained what the code needs to be 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
So claude had pointed out that in app.py where str(st.session_state.secret) ran on even-numbered attempts so then python took my guess to the secret as a text so for example "9" > "50"



- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.


so after claude made the edits it suggested, i saw that the code still didn't run well, meaning it was accurate to say go higher if you entered a negative number and 0 , and go lower if you entered over 100 but i told them to keep it restrcited to 1-100 and dont let it accept number that are not within that range
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided by having Claude explain to me the changes that was made. I f I saw that it didnt fix the bug, which for one of the changes that Claude code didn't i went and told them how the problem was still not fixed

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One of the manual test I ran was by running the code. I wanted to see if it gave acdurate hints and didn't accept numbers except from 1-100

- Did AI help you design or understand any tests? How?
It did and I had it explain what is this specific function for, and why change this particular line

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain streamlit reruns and session by saying that everytime you clicked something Steamlist run the whole program again from the start and basically answers or previous guesses dont get stored, its a whole restart


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Maybe testing habit and using git. And asking for explanation before asking for a fix which is what I did.
- What is one thing you would do differently next time you work with AI on a coding task?
I would check my setup next time before running anything because another one of my project was active in my terminal and claude was about to run it but I made sure to stop it before doing so

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think it's truly an amazing thing, however I do see how people can be over reliant on it, but it can really do an incredible job
