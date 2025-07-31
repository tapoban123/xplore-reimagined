import { Routes, Route, Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import Hero from "./components/Hero";
import Test from "./components/Test";
import Dashboard from "./components/Dashboard";
import Signup from "./components/auth/Signup";
import Login from "./components/auth/Login";

function App() {
  const { userData, token } = useSelector((state) => state.auth);

  const ProtectedRoute = ({ children }) => {
    if (!token) {
      return <Navigate to="/log-in" replace />;
    }
    return children;
  };

  return (
    <main className="min-h-screen bg-gray-50 text-gray-900">
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/sign-up" element={<Signup />} />
        <Route path="/log-in" element={<Login />} />
        {/* <Route path="/test" element={<Test />} /> */}

        {/* Protected Route */}
        <Route
          path="/test"
          element={
            <ProtectedRoute>
              <Test />
            </ProtectedRoute>
          }
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        {/* Redirect unknown routes */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </main>
  );
}

export default App;
