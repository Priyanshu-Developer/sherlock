"use client";
import Dashboard from "@/components/Dashboard";
import OrderTable from "@/components/LeadsTable";
import Snackbar from '@mui/joy/Snackbar';

import { Lead } from "@/utils";
import axios from "@/utils/axios";
import { useEffect, useState } from "react";

export default function LeadsPage() {
  const [leads, setLeads] = useState<Lead[]>([]);
  const [snackbarOpen, setSnackbarOpen] = useState(false);

  useEffect(() => {
    const fetchLeads = async () => {
      try {
        const response = await axios.get<Lead[]>('http://localhost:5000/leads/all');
        setLeads(response.data);
      } catch (err) {
        console.error("Error fetching leads:", err);
        setSnackbarOpen(true);
      }
    };
    fetchLeads();
  }, []);

  return (
    <>
      <Dashboard>
        <OrderTable rows={leads} />
      </Dashboard>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={() => setSnackbarOpen(false)}
        variant="soft"
        color="danger"
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        Failed to fetch leads. Please try again later.
      </Snackbar>
    </>
  );
}