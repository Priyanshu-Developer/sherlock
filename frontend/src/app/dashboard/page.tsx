"use client";
import Dashboard from "@/components/Dashboard";
import LeadsCharts from "@/components/LeadCharts";
import AgentCharts from "@/components/AgentCharts";

import { useEffect, useState } from "react";
import axios from "axios";
import { Lead } from "@/utils";



export default function DashboardPage() {
   const [leads, setLeads] = useState<Lead[]>([]);
  
    useEffect(() => {
    const fetchLeads = async () => {
      try {
        const response = await axios.get<Lead[]>('http://localhost:5000/leads/all');
        setLeads(response.data);
       
      } catch (err) {
        console.error("Error fetching leads:", err);
        // Optionally, you can handle the error here, e.g., show a notification
      
      }
    };

    fetchLeads();
  }, []);
  return (
   <Dashboard>
    
     <LeadsCharts data={leads} />
     <AgentCharts/>

   </Dashboard>
  );
}