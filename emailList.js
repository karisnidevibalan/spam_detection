import React from "react";
import EmailCard from "./EmailCard";

const EmailList = ({ emails }) => {
    return (
        <div>
            <h2>Detected Emails</h2>
            {emails.map((email) => (
                <EmailCard key={email.id} email={email} />
            ))}
        </div>
    );
};

export default EmailList;
