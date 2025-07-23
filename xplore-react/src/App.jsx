import { Routes, Route } from 'react-router-dom'
import Hero from './components/Hero'

import Test from './components/Test';
import Dashboard from './components/Dashboard';


function App() {
  

  return (
    <>
      <main>
      
        <Routes>
          <Route path='/' element={<Hero />} />
          <Route path='/test' element={<Test />} />
          <Route path="/dashboard" element={<Dashboard />} />
          
        </Routes>
        
      </main>
    </>
  )
}

export default App
