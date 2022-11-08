import React, { useEffect, useState } from 'react'
import axios from 'axios'
export const User = () => {
    const [user, setuser] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:8700/api/user').then(data => setuser(data.data.data))
    }, [])

    return (
        <div className='row my-5'>
            {
                user.map((us, i) => {
                    return (
                        <div className='col-lg-4' key={i}>
                            <div className="card" style={{ width: "18rem" }}>
                                <img src={us.imageUrl} className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h5 className="card-title">{us.name}</h5>
                                    <p className="card-text">Roll No </p>
                                    <a href="/" className="btn btn-primary">{us.rollNo}</a>
                                </div>
                            </div>
                        </div>
                    )
                })
            }
        </div>
    )
}