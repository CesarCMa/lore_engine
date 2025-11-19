import clsx from 'clsx';

export default function Input({
  type = 'text',
  value,
  onChange,
  placeholder,
  error,
  className,
  ...props
}) {
  return (
    <div className="w-full">
      <input
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className={clsx(
          'w-full bg-parchment-50 border-2 rounded-lg px-4 py-2 font-body',
          'focus:ring-2 focus:outline-none transition-colors duration-200',
          error
            ? 'border-crimson-500 focus:ring-crimson-500 focus:border-crimson-500'
            : 'border-gold-400 focus:ring-arcane-500 focus:border-arcane-500',
          className
        )}
        {...props}
      />
      {error && (
        <p className="text-crimson-600 text-sm mt-1">{error}</p>
      )}
    </div>
  );
}
