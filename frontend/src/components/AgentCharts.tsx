'use client';

import * as React from 'react';
import {
  Box,
  Typography,
  CircularProgress
} from '@mui/joy';
import {
  BarChart,
  PieChart,
  pieArcLabelClasses
} from '@mui/x-charts';
import { Agent } from '@/utils';
import axios from '@/utils/axios';

export default function LeadCharts() {
  const [agentLeads, setAgentLeads] = React.useState<Agent[]>([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    const fetchLeads = async () => {
      try {
        const response = await axios.get<{ data: Agent[] }>('http://localhost:5000/leads/agents');
        setAgentLeads(response.data.data || []);
      } catch (err) {
        console.error("Error fetching leads:", err);
      } finally {
        setLoading(false); // ✅ THIS WAS MISSING
      }
    };
    fetchLeads();
  }, []);

  const leadCounts = React.useMemo(() => {
    const agentMap: Record<string, number> = {};
    agentLeads.forEach(row => {
      if (row.agent) {
        agentMap[row.agent] = (agentMap[row.agent] || 0) + 1;
      }
    });

    return Object.entries(agentMap).map(([agent, count]) => ({
      agent,
      count,
    }));
  }, [agentLeads]);

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', py: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (leadCounts.length === 0) {
    return (
      <Typography  sx={{ textAlign: 'center', mt: 4 }}>
        No leads data available.
      </Typography>
    );
  }

  return (
    <Box sx={{ display: 'grid', gap: 4, mt: 4 }}>
      {/* Bar Chart */}
      <Box>
        <Typography level="h4" sx={{ mb: 2 }}>Leads per Agent</Typography>
        <BarChart
          xAxis={[{
            scaleType: 'band',
            data: leadCounts.map(d => d.agent),
            label: 'Agent',
          }]}
          series={[{
            data: leadCounts.map(d => d.count),
            label: 'Leads',
            color: '#1976d2'
          }]}
          width={600}
          height={300}
        />
      </Box>

      {/* Pie Chart */}
      <Box>
        <Typography level="h4" sx={{ mb: 2 }}>Lead Distribution by Agent</Typography>
        <PieChart
          series={[{
            arcLabel: (item) => `${item.value}`,
            data: leadCounts.map(d => ({
              id: d.agent,
              value: d.count,
              label: d.agent,
            })),
            innerRadius: 50,
            outerRadius: 100,
            paddingAngle: 2,
            cornerRadius: 4,
            startAngle: -90,
            endAngle: 270,
          }]}
          sx={{
            [`& .${pieArcLabelClasses.root}`]: {
              fill: 'white',
              fontWeight: 'bold',
            },
          }}
          width={600}
          height={300}
        />
      </Box>
    </Box>
  );
}
