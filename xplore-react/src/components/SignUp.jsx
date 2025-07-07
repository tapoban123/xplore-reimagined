import React from 'react'
import { useNavigate } from 'react-router-dom'

const SignUp = () => {
  const navigate = useNavigate();

  const ToLogin = () => {
    setTimeout(() => {
      navigate('/login'); 
    }, 500);
  };

  return (
    <div className='flex justify-center items-center h-screen'>
      <div className="w-80 rounded-lg shadow h-auto p-6 bg-white relative overflow-hidden">
        <div className="flex flex-col justify-center items-center space-y-2">
          <h2 className="text-2xl font-medium text-slate-700">Sign Up</h2>
          <p className="text-slate-500">Enter details below.</p>
        </div>
        <form className="w-full mt-4 space-y-3">
          <div>
            <input
              className="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
              placeholder="Username"
              id="username"
              name="username"
              type="text"
              required
            />
          </div>
          <div>
            <input
              className="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
              placeholder="Email"
              id="email"
              name="email"
              type="email"
              required
            />
          </div>
          <div>
            <input
              className="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
              placeholder="Password"
              id="password"
              name="password"
              type="password"
              required
            />
          </div>

          <button
            className="w-full cursor-pointer justify-center py-1 bg-blue-500 hover:bg-black active:bg-blue-700 rounded-md text-white ring-2"
            id="login"
            name="login"
            type="submit"
          >
            Sign Up
          </button>
          <p className="flex justify-center space-x-1">
            <span className="text-slate-700">Have an account?</span>
            <button
              type="button"
              onClick={ToLogin} 
              className="text-blue-500 hover:underline cursor-pointer"
            >
              Login
            </button>
          </p>
        </form>
      </div>
    </div>
  )
}

export default SignUp
