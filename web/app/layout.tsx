export const metadata = {
  title: 'ProtoLabs KB — Agentic Manufacturing Intelligence',
  description: 'Chat with ProtoLabs DFM, strategy, and governance agents powered by manufacturing knowledge.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet" />
      </head>
      <body className="font-sans">{children}</body>
    </html>
  );
}
