import { Routes, Route } from 'react-router-dom'
import Hero from './components/Hero'
import SignUp from './components/SignUp';
import Login from './components/Login';
import Test from './components/Test';
import Dashboard from './components/Dashboard';


function App() {
  

  return (
    <>
      <main className='bg-black min-h-screen'>
      
        <Routes>
          <Route path='/' element={<Hero />} />
          <Route path='/signup'  element={<SignUp />}/>
          <Route path='/login' element={<Login />} />
          <Route path='/test' element={<Test />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
        
      </main>
    </>
  )
}

export default App
