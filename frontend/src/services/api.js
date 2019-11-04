import axios from 'axios';

const api = axios.create({
    baseURL: 'https://search-city.herokuapp.com/',
});

export default api;