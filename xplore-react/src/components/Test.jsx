import React, { useEffect, useState } from 'react'
import '../index.css'
import fetchQuestion from './../assets/question';
import { useNavigate } from "react-router-dom";
import Dashboard from './Dashboard';



const Test = () => {
  const [index,setIndex] = useState(0);
  const [questions,setQuestions] = useState([]);
  const [answers,setAnswers] = useState([]);
  const [currentAnswer,setCurrentAnswer] = useState(null);
  
const navigate = useNavigate();

  useEffect(()=>{
  const alreadyFetch = sessionStorage.getItem('questionsFetched')

  if(!alreadyFetch){
  const getQuestions = async ()=>{
    try {
      const data = await fetchQuestion();
      setQuestions(data.all_questions);
      sessionStorage.setItem('questionsFetched','true');

    } catch (error) {
      console.error(error);
    }
  }
  getQuestions();
}
},[])


//if (!questions.length) return <div>Loading...</div>;

const question = questions?.[index] || {};

const result = {
  questions_with_answers: answers
};

function handleSubmit(){
  console.log(result);
  navigate('/dashboard');
}

console.log('current question',question);

  return (
    <>
      <div className='pattern-bg h-screen w-screen  flex items-center justify-center '>
        <div className='w-[700px] m-auto  bg-white text-[#262626] flex flex-col gap-5 rounded-[20px] pt-10 pb-10 pl-20 pr-20'>
          <h1 className='text-3xl font-bold'>Let’s Understand You!</h1>
          <hr className='h-[2px] rounded-none bg-[#707070]' />
          <h2 className='text-[25px] font-medium'>{index+1}. {question.question}</h2>
          <ul>
            { Array.isArray(question.choices) && 
              question.choices.map((choice,index)=>(
                <li className={`flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 
                 ${currentAnswer === choice ? 'bg-purple-200 border-purple-600' : 'border-[#686868] hover:bg-gray-100'}`}
                  onClick={() => setCurrentAnswer(choice)}
                >
              {choice}
            </li>
              ))
            }
          </ul>
          <button className='m-auto w-30 cursor-pointer h-[40px] bg-[#553f9a] text-white text-[15px] font-medium rounded-sm nextBtn relative'
          onClick={()=>{
            if (!currentAnswer) return;
            const updatedAnswers = [...answers, {
            question: question.question,
            answer: currentAnswer
          }];
           setAnswers(updatedAnswers);
           {index!=20 && setIndex(prev => prev + 1)}

           if (index === questions.length - 1) {
              handleSubmit(); 
  }
          }}
          >{index!=20 ? 'Next' : 'Submit'}</button>
          <div className='index'>{index + 1} of {questions.length} questions</div>
        </div>
      </div>
    </>
  )
}

export default Test