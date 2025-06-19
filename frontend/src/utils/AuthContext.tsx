"use client";
import React, { createContext, useContext, useEffect, useState, ReactNode } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";

interface Admin {
  id: number;
  username: string;
  email: string;
  // Add more fields as needed
}

interface AuthContextType {
  admin: Admin | null;
  setAdmin: (admin: Admin | null) => void;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [admin, setAdminState] = useState<Admin | null>(null);
  const router = useRouter();

  // Initialize from localStorage on mount
  useEffect(() => {
    const stored = localStorage.getItem("admin");
    if (stored) {
      setAdminState(JSON.parse(stored));
    }
  }, []);

  // Wrapper to update both state and localStorage
  const setAdmin = (admin: Admin | null) => {
    if (admin) {
      localStorage.setItem("admin", JSON.stringify(admin));
    } else {
      localStorage.removeItem("admin");
    }
    setAdminState(admin);
  };

  const logout = async () => {
    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/logout`, {}, {
        withCredentials: true,
      });
    } catch (err) {
      console.error("Logout error:", err);
    } finally {
      setAdmin(null);
      router.push("/login");
    }
  };

  return (
    <AuthContext.Provider value={{ admin, setAdmin, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
};
