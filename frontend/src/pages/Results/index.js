import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom'
import api from '../../services/api';

import './styles.css';

export default function Results(){
    
    const [results, setResults] = useState([])

    useEffect(() => {
        async function loadResults(){
            const response = await api.get('./texto/1');
            console.log(response.data)
            setResults(response.data);
        }    
    }, [])
    
    return (
        <>
            <ul className="result-list">
                
                
                {results.map(result => (
                    <Link to="/details">
                        <li key={result._id}>
                            <strong>{result.Titulo}</strong>
                            <span>Relevância: {result.Texto}</span>

                        </li>
                    </Link>
                ))}
                
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