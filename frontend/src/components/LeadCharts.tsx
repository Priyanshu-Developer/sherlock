"use client";
import React from 'react';
import { Box, Typography, Card } from '@mui/joy';
import {
  BarChart,

} from '@mui/x-charts';

import { Lead } from '@/utils';
export default function LeadsCharts({ data }: { data: Lead[] }) {
  // === Leads per Status ===
  const statusMap = new Map<number, number>();
  data.forEach((row) => {
    statusMap.set(row.stage, (statusMap.get(row.stage) || 0) + 1);
  });

  const statusKeys = Array.from(statusMap.keys()).sort();
  const statusValues = statusKeys.map((stage) => statusMap.get(stage) || 0);

  // === Leads per Day ===
  const dayMap = new Map<string, number>();
  data.forEach((row) => {
    dayMap.set(row.date, (dayMap.get(row.date) || 0) + 1);
  });

  const dayKeys = Array.from(dayMap.keys()).sort((a, b) => new Date(a).getTime() - new Date(b).getTime());
  const dayValues = dayKeys.map((date) => dayMap.get(date) || 0);

  return (
    <Box sx={{ display: 'grid', gap: 4, mt: 4 }}>
      {/* Leads Per Status */}
      <Card>
        <Typography level="h4" gutterBottom>Leads per Status</Typography>
        <BarChart
          xAxis={[{ id: 'stage', data: statusKeys, label: 'Status' }]}
          series={[{ data: statusValues, label: 'Leads', color: '#007FFF' }]}
          height={300}
        />
      </Card>

      {/* Leads Per Day */}
      <Card>
        <Typography level="h4" gutterBottom>Leads per Day</Typography>
        <BarChart
          xAxis={[{ id: 'day', data: dayKeys, label: 'Date', scaleType: 'band' }]}
          series={[{ data: dayValues, label: 'Leads', color: '#00C49F' }]}
          height={300}
        />
      </Card>

     
    </Box>
  );
}
