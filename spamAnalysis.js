import React from "react";
import { PieChart, Pie, Tooltip } from "recharts";

const SpamAnalysis = ({ emails }) => {
    const data = [
        { name: "Spam", value: emails.filter(e => e.isSpam).length, fill: "#FF6347" },
        { name: "Safe", value: emails.filter(e => !e.isSpam).length, fill: "#32CD32" },
    ];

    return (
        <PieChart width={400} height={300}>
            <Pie data={data} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80} />
            <Tooltip />
        </PieChart>
    );
};

export default SpamAnalysis;
