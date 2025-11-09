export const metadata = { title: "second-brain" };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: "system-ui, sans-serif", padding: 0, margin: 0 }}>
        {children}
      </body>
    </html>
  );
}
