import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignUp = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });

  const ToLogin = () => {
    setTimeout(() => {
      navigate('/login'); 
    }, 500);
  };

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/api/auth/signup', {
        name: formData.username,
        email: formData.email,
        password: formData.password
      });
      navigate('/test'); // Redirect after successful signup
    } catch (error) {
      alert(error.response?.data?.message || "Signup failed");
    }
  };

  return (
    <div className='flex justify-center items-center h-screen'>
      <div className="w-80 rounded-lg shadow h-auto p-6 bg-white relative overflow-hidden">
        <div className="flex flex-col justify-center items-center space-y-2">
          <h2 className="text-2xl font-medium text-slate-700">Sign Up</h2>
          <p className="text-slate-500">Enter details below.</p>
        </div>
        <form className="w-full mt-4 space-y-3" onSubmit={handleSubmit}>
          <div>
            <input
              className="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
              placeholder="Username"
              id="username"
              name="username"
              type="text"
              value={formData.username}
              onChange={handleChange}
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
              value={formData.email}
              onChange={handleChange}
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
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <button
            className="w-full cursor-pointer justify-center py-1 bg-blue-500 hover:bg-black active:bg-blue-700 rounded-md text-white ring-2"
            id="signup"
            name="signup"
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
  );
};

export default SignUp;
