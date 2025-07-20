import axios from 'axios';


const fetchQuestion = async ()=>{
    try {
        const res = await axios.get('/api/ai/questions')
        console.log('axios response:',res.data);
        return res.data;
    } catch (error) {
        console.error('Error while fetching question:',error);
    }
}


export default fetchQuestion;