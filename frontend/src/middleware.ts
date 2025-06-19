import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  console.log(`Middleware triggered for ${pathname}`);

  const PUBLIC_PATHS = ['/login', '/register', '/_next', '/favicon.ico'];
  const isPublic = PUBLIC_PATHS.some((path) => pathname.startsWith(path));

  const token = request.cookies.get('auth_token')?.value;
  console.log(`Token found: ${token}`);
  console.log(`Is public path: ${isPublic}`);

  // 🔒 If not logged in and trying to access protected route → redirect to login
  if (!isPublic && !token) {
    const loginUrl = request.nextUrl.clone();
    loginUrl.pathname = '/login';
    console.log(`Redirecting to login: ${loginUrl}`);
    return NextResponse.redirect(loginUrl);
  }

  // 🧭 If logged in and trying to access login/register → redirect to dashboard
  if (isPublic && token && (pathname === '/login')) {
    const dashboardUrl = request.nextUrl.clone();
    dashboardUrl.pathname = '/dashboard';
    console.log(`Redirecting to dashboard: ${dashboardUrl}`);
    return NextResponse.redirect(dashboardUrl);
  }

  // ✅ Default: allow access
  console.log(`Access granted to: ${pathname}`);
  return NextResponse.next();
}
