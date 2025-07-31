import axios from "axios";

const fetchSignup = async (data) => {
  try {
    const res = await axios.post("/api/student/auth/sign-up", {
      name: data.name,
      email: data.email,
      password: data.password,
    });

    return res.data;
  } catch (error) {
    console.error(
      "Error while signing up student:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export default fetchSignup;