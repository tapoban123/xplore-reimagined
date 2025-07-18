import React from 'react'
import '../index.css'

const Test = () => {
  return (
    <>
      <div className='pattern-bg h-screen w-screen  flex items-center justify-center '>
        <div className='w-[700px] m-auto  bg-white text-[#262626] flex flex-col gap-5 rounded-[20px] pt-10 pb-10 pl-20 pr-20'>
          <h1 className='text-3xl font-bold'>Let’s Understand You!</h1>
          <hr className='h-[2px] rounded-none bg-[#707070]' />
          <h2 className='text-[25px] font-medium'>1. This is a question </h2>
          <ul>
            <li className='flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 '>
              1
            </li>
            <li className='flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 '>
              2
            </li>
            <li className='flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 '>
              3
            </li>
            <li className='flex items-center h-12 px-4 border border-[#686868] rounded-md text-base cursor-pointer hover:bg-gray-100 m-2 '>
              4
            </li>
          </ul>
          <button className='m-auto w-30 h-[40px] bg-[#553f9a] text-white text-[15px] font-medium rounded-sm nextBtn relative'>Next</button>
          <div className='index'>1 of 19 questions</div>
        </div>
      </div>
    </>
  )
}

export default Test