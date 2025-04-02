import React, { useState, useEffect } from "react";
import EmailList from "../components/EmailList";
import SpamAnalysis from "../components/SpamAnalysis";
import axios from "axios";

const Dashboard = () => {
    const [emails, setEmails] = useState([]);

    useEffect(() => {
        axios.get("https://api.example.com/spam-emails")
            .then((res) => setEmails(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h1>Email Spam Detector</h1>
            <SpamAnalysis emails={emails} />
            <EmailList emails={emails} />
        </div>
    );
};

export default Dashboard;
