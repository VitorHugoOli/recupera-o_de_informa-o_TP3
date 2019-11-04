import React, {useEffect, useState} from 'react';
import api from '../../services/api';

import './styles.css';

export default function Details(){

    const [detail, setDetail] = useState([])

    useEffect(() => {
        async function loadDetails(){
            const response = await api.get('./search', {
                
            });
            console.log(response.data)
            setDetail(response.data);
        }    
    }, [])

    return (
        <div className='filedetail'>
            <strong>{detail.Titulo}</strong>
            <p>{detail.Texto}</p>
        </div>
    )
}

//<strong>{detail.Titulo}</strong>
//<span>{detail.Texto}</span>