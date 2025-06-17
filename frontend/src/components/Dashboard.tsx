"use client";
import * as React from 'react';
import { CssVarsProvider } from '@mui/joy/styles';
import CssBaseline from '@mui/joy/CssBaseline';
import Box from '@mui/joy/Box';
import Breadcrumbs from '@mui/joy/Breadcrumbs';
import Link from '@mui/joy/Link';
import Typography from '@mui/joy/Typography';
import DashboardRoundedIcon from '@mui/icons-material/DashboardRounded';
import PersonIcon from '@mui/icons-material/Person';

import AssignmentRoundedIcon from '@mui/icons-material/AssignmentRounded';
import QuestionAnswerRoundedIcon from '@mui/icons-material/QuestionAnswerRounded';
import GroupRoundedIcon from '@mui/icons-material/GroupRounded';
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';
import ChevronRightRoundedIcon from '@mui/icons-material/ChevronRightRounded';
import PersonSearchRoundedIcon from '@mui/icons-material/PersonSearchRounded';


import Sidebar, { MenuProps } from  "@/components/Sidebar";
import Header from '@/components/Header';
import { usePathname } from 'next/navigation';

const menuItems: MenuProps[] = [
  {
    title: 'Home',
    icon: <HomeRoundedIcon />,
    segment: 'home',
  },
  {
    title: 'Dashboard',
    icon: <DashboardRoundedIcon />,
    segment: '/dashboard',
  },
  {
    title: 'Leads',
    icon: <PersonSearchRoundedIcon />,
    segment: '/dashboard/leads',
  },
  {
    title: 'Agents',
    icon: <PersonIcon />,
    segment: '/dashboard/agents',
   
  },
  {
    title: 'Messages',
    icon: <QuestionAnswerRoundedIcon />,
    segment: 'messages',
  },
  {
    title: 'Users',
    icon: <GroupRoundedIcon />,
    segment: 'users',
    children: [
      { title: 'My profile', segment: 'my-profile',icon: <AssignmentRoundedIcon /> },
      { title: 'Create a new user', segment: 'create-user',icon: <AssignmentRoundedIcon /> },
      { title: 'Roles & permission', segment: 'roles-permission',icon: <AssignmentRoundedIcon /> },
    ],
  },
];

function formatSegment(segment: string): string {

  return segment
    .replace(/-/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function AutoBreadcrumbs({ pathname }: { pathname: string }) {
  const pathSegments: string[] = pathname.split("/").filter(Boolean); // removes empty strings

  return (
    <>
      {pathSegments.map((segment: string, index: number) => {
        const href: string = "/" + pathSegments.slice(0, index + 1).join("/");
        const isLast: boolean = index === pathSegments.length - 1;

        return isLast ? (
          <Typography
            key={href}
            color="primary"
            sx={{ fontWeight: 500, fontSize: 12 }}
          >
            {formatSegment(segment)}
          </Typography>
        ) : (
          <Link
            key={href}
            underline="hover"
            color="neutral"
            href={href}
            sx={{ fontSize: 12, fontWeight: 500 }}
          >
            {formatSegment(segment)}
          </Link>
        );
      })}
    </>
  );
}

export default function Dashboard({children,headChildren}: {children: React.ReactNode,headChildren?: React.ReactNode}) {
    const pathname = usePathname(); // e.g., "/dashboard/orders"
  return (
    <CssVarsProvider disableTransitionOnChange>
      <CssBaseline />
      <Box sx={{ display: 'flex', minHeight: '100dvh' }}>
        <Header />
        <Sidebar menuItems={menuItems} pathname={pathname}/>
        <Box
          component="main"
          className="MainContent"
          sx={{
            px: { xs: 2, md: 6 },
            pt: {
              xs: 'calc(12px + var(--Header-height))',
              sm: 'calc(12px + var(--Header-height))',
              md: 3,
            },
            pb: { xs: 2, sm: 2, md: 3 },
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            minWidth: 0,
            height: '100dvh',
            gap: 1,
          }}
        >
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            <Breadcrumbs
              size="sm"
              aria-label="breadcrumbs"
              separator={<ChevronRightRoundedIcon  />}
              sx={{ pl: 0 }}
            >
              <Link
                underline="none"
                color="neutral"
                href="#some-link"
                aria-label="Home"
              >
                <HomeRoundedIcon />
              </Link>
              <AutoBreadcrumbs pathname={pathname} />
            </Breadcrumbs>
          </Box>
          <Box sx={{  display: 'flex',  mb: 1,  gap: 1,  flexDirection: { xs: 'column', sm: 'row' },  alignItems: { xs: 'start', sm: 'center' },  flexWrap: 'wrap',  justifyContent: 'space-between', }}  >
            <Typography level="h2" component="h1">{formatSegment(pathname.split('/').pop() || '')}  </Typography>
            {headChildren}
          </Box>
          <Box height='100dvh' sx={{ overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: 2 }}>
          {children}
          </Box>
        </Box>
      </Box>
    </CssVarsProvider>
  );
}