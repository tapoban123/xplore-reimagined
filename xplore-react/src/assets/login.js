import axios from "axios";

const fetchLogin = async (data) => {
  try {
    const res = await axios.post("/api/student/auth/login", {
      email: data.email,
      password: data.password,
    });

    return res.data;
  } catch (error) {
    console.error(
      "Error while logging in student:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export default fetchLogin;