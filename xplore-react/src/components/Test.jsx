import React, { useEffect, useState } from 'react'
import '../index.css'
import fetchQuestion from './../assets/question';



const Test = () => {
  const [index,setIndex] = useState(0);
  const [questions,setQuestions] = useState([])
  


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

if (!questions.length) return <div>Loading...</div>;

const question = questions[index];

console.log('current question',question);

  return (
    <>
      <div className='pattern-bg h-screen w-screen  flex items-center justify-center '>
        <div className='w-[700px] m-auto  bg-white text-[#262626] flex flex-col gap-5 rounded-[20px] pt-10 pb-10 pl-20 pr-20'>
          <h1 className='text-3xl font-bold'>Let’s Understand You!</h1>
          <hr className='h-[2px] rounded-none bg-[#707070]' />
          <h2 className='text-[25px] font-medium'>{index+1}. {question.question}</h2>
          <ul>
            {
              question.choices.map((choice,index)=>(
                <li className='flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 ' >
              {choice}
            </li>
              ))
            }
          </ul>
          <button className='m-auto w-30 h-[40px] bg-[#553f9a] text-white text-[15px] font-medium rounded-sm nextBtn relative'>Next</button>
          <div className='index'>1 of 19 questions</div>
        </div>
      </div>
    </>
  )
}

export default Test