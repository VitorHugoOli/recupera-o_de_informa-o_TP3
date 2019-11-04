import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom'
import api from '../../services/api';

import './styles.css';

export default function Results(){
    
    const [results, setResults] = useState([])

    useEffect(() => {
        async function loadResults(){
            const response = await api.get('./search', {
                
            });
            console.log(response.data)
            setResults(response.data);
        }    
    }, [])
    
    return (
        <>
            <ul className="result-list">
                <Link to="/details">
                <li>
                    <strong>Um título qualquer</strong>
                    <span>Relevância: 3.0000</span>
                </li>
                </Link>
                <li>
                    <strong>Um título qualquer</strong>
                    <span>3.0000</span>
                </li>
                <li>
                    <strong>Um título qualquer</strong>
                    <span>3.0000</span>
                </li>
                
            </ul>
        </>
    )
}

/*{results.map(result => (
    <li key={result._id}>
        <strong>{result.title}</strong>
        <span>Relevância: {result.relevance}</span>

    </li>
))}*/